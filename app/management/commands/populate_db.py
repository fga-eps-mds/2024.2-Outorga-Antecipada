from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Usuario, Cargo, Tipo, Componente, Kit, KitComponente, HistoricoProducao

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais'

    def handle(self, *args, **kwargs):
        # Populando a Tabela Cargo
        Cargo.objects.get_or_create(descricao="ADMIN")
        Cargo.objects.get_or_create(descricao="OPERADOR")
       
        # Populando a tabela Tipo
        amarelo, created = Tipo.objects.get_or_create(nome="AMARELO")
        azul, created = Tipo.objects.get_or_create(nome="AZUL")
        preto, created = Tipo.objects.get_or_create(nome="PRETO")
        
        # Populando a tabela Componente
        tampa_amarela, created = Componente.objects.get_or_create(nome="TAMPA", id_tipo=amarelo)
        tampa_azul, created = Componente.objects.get_or_create(nome="TAMPA", id_tipo=azul)
        tampa_preta, created = Componente.objects.get_or_create(nome="TAMPA", id_tipo=preto)

        # Populando a tabela Kit
        kit1, created = Kit.objects.get_or_create(nome="KIT 1", peso=10)
        kit2, created = Kit.objects.get_or_create(nome="KIT 2", peso=15)
        kit3, created = Kit.objects.get_or_create(nome="KIT 3", peso=20)

        # Populando a Tabela KitComponente
        KitComponente.objects.get_or_create(id_kit=kit1, id_componente=tampa_amarela, defaults={'qtd_pecas': 1})
        KitComponente.objects.get_or_create(id_kit=kit1, id_componente=tampa_azul, defaults={'qtd_pecas': 2})
        KitComponente.objects.get_or_create(id_kit=kit1, id_componente=tampa_preta, defaults={'qtd_pecas': 1})

        KitComponente.objects.get_or_create(id_kit=kit2, id_componente=tampa_amarela, defaults={'qtd_pecas': 3})
        KitComponente.objects.get_or_create(id_kit=kit2, id_componente=tampa_azul, defaults={'qtd_pecas': 2})
        KitComponente.objects.get_or_create(id_kit=kit2, id_componente=tampa_preta, defaults={'qtd_pecas': 1})

        KitComponente.objects.get_or_create(id_kit=kit3, id_componente=tampa_amarela, defaults={'qtd_pecas': 1})
        KitComponente.objects.get_or_create(id_kit=kit3, id_componente=tampa_azul, defaults={'qtd_pecas': 2})
        KitComponente.objects.get_or_create(id_kit=kit3, id_componente=tampa_preta, defaults={'qtd_pecas': 2})

        # Populando HistoricoProducao
        now = timezone.now()
        HistoricoProducao.objects.get_or_create(id_kit=kit1, hora_producao=now, defaults={'qtd_pecas': 4})
        HistoricoProducao.objects.get_or_create(id_kit=kit2, hora_producao=now, defaults={'qtd_pecas': 6})
        HistoricoProducao.objects.get_or_create(id_kit=kit3, hora_producao=now, defaults={'qtd_pecas': 5})

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
