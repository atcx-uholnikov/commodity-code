from django.shortcuts import render
from .models import Goods, DuesRate
from django.views.generic import ListView
from fuzzywuzzy import fuzz

class IndexView(ListView):
    model = Goods
    template_name = 'index.html'
    queryset=Goods.objects.all()
    context_object_name = 'goods'

class SearchCode(ListView):
    model: Goods
    template_name = "hscode.html"
    context_object_name = "goods"

    def get_queryset(self):
        query = self.request.GET.get('q')
        report = "Ви не ввели запит для пошуку.\nПовторіть спробу"

        if query == "": # IF REQUEST IS EMPTY
            return

        elif query.isdigit(): # IF REQUEST IS A DIGIT
            results = Goods.objects.filter(code__icontains=query)

            totalranks = {}
            dues = {}

            for n in results:
                rank = fuzz.ratio(query, n.code)
                totalranks[n.id] = (rank)
                dues_rate = DuesRate.objects.filter(code__icontains=n.code)
                dues[n.id] = dues_rate

            sorted_totalranks = dict(sorted(totalranks.items(),key=lambda item: item[1],reverse=True))

            output = [results, len(results), query, sorted_totalranks, dues]
            return output

        else: # IF REQUEST IS A STRING

            test_results = Goods.objects.filter(description__iregex=query[:-1])

            def more_results(h, n):

                if len(h) >= 10 or len(n.split()) == 1:
                    return n
                else:
                    n = n.rsplit(' ', 1)[0]
                    h = Goods.objects.filter(description__iregex=n[:-1]).order_by("-date")
                    return more_results(h, n)

            results = Goods.objects.filter(description__iregex=more_results(test_results, query)[:-1])

            totalranks = {}
            dues = {}

            for p in results:

                dues_rate = DuesRate.objects.filter(code__icontains=p.code)
                dues[p.id] = dues_rate

                searchranks = []
                indexpos = []

                for u in p.description.split():
                    for m in query.split():
                        if m.lower()[:-1] in u.lower() and (len(u) - len(m)) < 4 and m.lower() not in ["з", "із", "для", "над", "через", "під", "від"]:
                            word = u.lower().replace(":", "").replace(",", "").replace(".", "").replace('"', "").replace('(', "").replace(')', "")
                            indexpos.append(p.description.split().index(u))
                            distance_index = 100 / len(p.description.split())
                            distance_delta = len(p.description.split()) - indexpos[-1] + (indexpos[0] - 1)

                            if len(indexpos) > 1 and (indexpos[-1] - indexpos[-2]) >= 3:
                                searchranks.append((fuzz.ratio(m.lower(), word)) * ((distance_delta * distance_index) / 100))
                            else:
                                searchranks.append(fuzz.ratio(m.lower(), word))
                        else:
                            pass

                for k in range(len(query.split()) - len(searchranks)):
                    searchranks.append(0)

                if len(searchranks) == 0:
                    totalranks[p.id] = 0
                else:
                    totalranks[p.id] = round(sum(searchranks) / len(searchranks))

            sorted_totalranks = dict(sorted(totalranks.items(),key=lambda item: item[1],reverse=True))

            if sum(sorted_totalranks[x] for x in sorted_totalranks) > 1:
                zero = sum(x == 0 for x in sorted_totalranks.values())
                output = [results, len(results)-zero, query.lower(), sorted_totalranks, dues]
            else:
                output = ["zero"]

            return output