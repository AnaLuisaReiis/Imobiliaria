from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db import connection
from .models import Visita
from .forms import VisitaForm
from .models import Imovel,Apartamento,Casa,Visita
def home(request):
    return render(request,'imoveis/home.html')

def lista_imoveis(request):
    return render(request,'imoveis/imoveis.html')

def imoveis(request):
    
    if request.method == 'POST':
        tipo_imovel = request.POST.get('tipo_imovel')
        
        # Criando o objeto Imovel
        novo_imovel = Imovel(
            tipo_imovel=tipo_imovel,
            nome_proprietario=request.POST.get('nome_proprietario'),
            endereco=request.POST.get('endereco'),
            quantidade_quartos=request.POST.get('quantidade_quartos'),
            quantidade_suites=request.POST.get('quantidade_suites'),
            quantidade_salas_estar=request.POST.get('quantidade_salas_estar'),
            vagas_garagem=request.POST.get('vagas_garagem'),
            area=request.POST.get('area'),
            armario_embutido=request.POST.get('armario_embutido') == 'sim',  # Exemplo para BooleanField
            descricao=request.POST.get('descricao', ''),
            imagem_imovel=request.FILES.get('imagem_imovel')
        )
        print(request.POST.get('imagem_imovel'))
        novo_imovel.save()

        # Verificando se é casa ou apartamento e salvando na tabela correspondente
        if tipo_imovel == 'casa':
            Casa.objects.create(imovel=novo_imovel)
        elif tipo_imovel == 'apartamento':
            Apartamento.objects.create(
                imovel=novo_imovel,
                quantidade_salas_jantar=request.POST.get('quantidade_salas_jantar'),
                andar=request.POST.get('andar'),
                valor_condominio=request.POST.get('valor_condominio'),
                portaria_24h=request.POST.get('portaria_24h') == 'sim'  # Exemplo para BooleanField
            )
        # Exibir todos os usuarios ja cadastrados
        imoveis = {
            'imoveis' : Imovel.objects.all()
        }

    return render(request,'imoveis/imoveis.html',imoveis)


def cadastro_visitas(request):
    if request.method == 'POST':
        imovel_id = request.POST.get('id_imovel')
        print('Imovel id')
        print(imovel_id)
        endereco = request.POST.get('endereco')
        print('endereco')
        print(endereco)
        data_visita = request.POST.get('dataVisita')
        print('data visita')
        print(data_visita)
        horario_visita = request.POST.get('horarioVisita')
        print('horario visita')
        print(horario_visita)
        
        # Adicionando prints para depuração
        print(f"Imóvel ID: {imovel_id}")
        print(f"Endereço: {endereco}")
        print(f"Data da visita: {data_visita}")
        print(f"Horário da visita: {horario_visita}")

        try:
            # Tentar buscar o imóvel pelo ID
            imovel = Imovel.objects.get(id_imovel=imovel_id)
            print(f"Imóvel encontrado: {imovel}")
            
            # Criar uma nova visita
            nova_visita = Visita(
                endereco=endereco,
                imovel=imovel,
                data_visita=data_visita,  # Validar o formato correto de data
                horario_visita=horario_visita,
            )
            nova_visita.save()
            print("Visita cadastrada com sucesso.")
            return redirect('lista_visitas')  # Redireciona para a lista de visitas

        except Imovel.DoesNotExist:
            print("Imóvel não encontrado.")
            return render(request, 'imoveis/cadastro_visitas.html', {'erro': 'Imóvel não encontrado.'})

    # Obter endereços únicos para exibir no formulário
    enderecos_unicos = Imovel.objects.values_list('endereco', flat=True).distinct()

    context = {
        'enderecos_unicos': enderecos_unicos,
    }
    return render(request, 'imoveis/cadastro_visitas.html', context)



def filtrar_imoveis(request):
    endereco = request.GET.get('endereco')
    
    # Filtrar imóveis com base no endereço
    imoveis = Imovel.objects.filter(endereco=endereco).values('id_imovel', 'tipo_imovel', 'endereco')

    return JsonResponse({'imoveis': list(imoveis)})

    
def lista_visitas(request):
    visitas = Visita.objects.all()
    context = {
        'visitas': visitas
    }
    return render(request, 'imoveis/lista_visitas.html', context)
   
   
