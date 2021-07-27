from django.shortcuts import render
from .forms import NameForm

from .logic.json_rpc_logic import get_external_api_data


def index(request):
    form = NameForm(initial={'method_name': 'auth.check'})
    if request.POST:
        external_api_data = get_external_api_data(request)

        return render(request, 'api_view.html', context={'api_data': external_api_data, 'form': form})
    return render(request, 'api_view.html', context={'form': form})



