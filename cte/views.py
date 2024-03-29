from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lancamento
from .forms import CteForm

@login_required
def ctes_list(request):
    ctes = Lancamento.objects.all()
    return render(request, 'cte_list.html', {'ctes': ctes})

@login_required
def ctes_new(request):
    form = CteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ctes_list')
    return render(request, 'cte_form.html', {'form': form})

@login_required
def ctes_update(request, id):
    cte = get_object_or_404(Lancamento, pk=id)
    form = CteForm(request.POST or None, instance=cte)

    if form.is_valid():
        form.save()
        return redirect('ctes_list')

    return render(request, 'cte_form.html', {'form': form})

@login_required
def ctes_delete(request, id):
    cte = get_object_or_404(Lancamento, pk=id)
    form = CteForm(request.POST or None, instance=cte)

    if request.method == 'POST':
        cte.delete()
        return redirect('ctes_list')

    return render(request, 'cte_delete_confirm.html', {'form': form})