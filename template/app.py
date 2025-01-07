import __init__
from view.view import SubscriptionService
from model.database import engine
from model.model import Subscription
from datetime import datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)

    def start(self):
        while True:
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Efetuar pagamento
            [0] -> Sair
            ''')

            choice = int(input('Escolha uma opção: '))

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_value()
            elif choice == 4:
                self.subscription_service.gen_chart()
            elif choice == 5:
                self.add_payment()
            else:
                break


    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = datetime.strptime(input('Data de assinatura: '),'%d/%m/%Y')
        valor = Decimal(input('Valor: '))
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)

        self.subscription_service.create(subscription)

    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        print('Escolha qual assinatura deseja excluir')
        print('0 -> Voltar')

        for i in subscriptions:
            print(f'{i.id} -> {i.empresa}')

        choice = int(input('Escolha a assinatura: '))

        if choice == 0:
            return

        self.subscription_service.delete(choice)
        print('Assinatura cancelada com sucesso!')

    def total_value(self):
        print(f'Seu valor total mensal de assinaturas é: {self.subscription_service.total_value()}')

    def add_payment(self):
        subscriptions = self.subscription_service.list_all()
        print('Escolha qual assinatura pagar')
        print('0 -> Voltar')

        for i in subscriptions:
            print(f'{i.id} -> {i.empresa}')

        choice = int(input('Escolha a assinatura: '))

        if choice == 0:
            return

        subscription = next((s for s in subscriptions if s.id == choice), None)

        if subscription is None:
            print('Assinatura não encontrada!')
            return

        self.subscription_service.pay(subscription)


UI().start()
