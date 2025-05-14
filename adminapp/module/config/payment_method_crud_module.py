from mainapp import models as mm
from mainapp.selectors.common_functions import message
from django.db.models import F

class PaymentTypeModule:

    def __init__(self, data):
        self.data = data

    def create_payment_type(self):
        try:
            payment_type_name = self.data['paymentTypeName']
            mm.PaymentType.objects.create(PaymentTypeName=payment_type_name)
            return message('Payment type created successfully'), 201
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def get_all_payment_types(self):
        return mm.PaymentType.objects.all().values(
            paymentTypeId=F('PaymentTypeID'),
            paymentTypeName=F('PaymentTypeName')
        ), 200

    def get_payment_type_by_id(self):
        try:
            payment_type_id = self.data['paymentTypeId']
            return mm.PaymentType.objects.values(
                paymentTypeId=F('PaymentTypeID'),
                paymentTypeName=F('PaymentTypeName')
            ).get(PaymentTypeID=payment_type_id), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.PaymentType.DoesNotExist:
            return message('Payment type not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def update_payment_type(self):
        try:
            payment_type_name = self.data['paymentTypeName']
            payment_type_id = self.data['paymentTypeId']

            payment_type_obj = mm.PaymentType.objects.get(PaymentTypeID=payment_type_id)
            payment_type_obj.PaymentTypeName = payment_type_name
            payment_type_obj.save()

            return message('Payment type updated successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.PaymentType.DoesNotExist:
            return message('Payment type not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500

    def delete_payment_type(self):
        try:
            payment_type_id = self.data['paymentTypeId']
            mm.PaymentType.objects.get(PaymentTypeID=payment_type_id).delete()
            return message('Payment type deleted successfully'), 200
        except KeyError as key:
            return message(f'{key} is missing'), 404
        except mm.PaymentType.DoesNotExist:
            return message('Payment type not found'), 404
        except Exception as e:
            print(e)
            return message('Something went wrong'), 500
