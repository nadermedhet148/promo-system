from django.test import TestCase
import mock
from Promo.PromoService.PromoService import PromoService
from Promo.Repositories.PromoRepository import PromoRepository
from Users.Repositories.NormalUserRepository import NormalUserRepository
from Users.models import NormalUser
from Promo.models import Promo



class UserServiceTest(TestCase):
    
    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_create_promo_must_be_administrator_user_to_create_promotion(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        normalUserRepository.get_one_by_id.return_value = False
        
        result = promoService.create_promo(promoAmount=10,description='',promoType='test',startTime="2021-01-12",endTime="2021-10-12",isActive=True,normalUserId=1,creatorType="test")
        self.assertEqual(result.get('error') , 'sorry you must be administrator_user to create promotion')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_create_promo_normal_user_should_be_existed(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        normalUserRepository.get_one_by_id.return_value = False
        
        result = promoService.create_promo(promoAmount=10,description='',promoType='test',startTime="2021-01-12",endTime="2021-10-12",isActive=True,normalUserId=1,creatorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry this normal user isn\'t existed')


    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_create_promo_promoAmount_should_be_more_thant_zero(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        normalUserRepository.get_one_by_id.return_value =  NormalUser(username='test',pk =1,name='test',address='test',mobileNumber="01150")
        
        result = promoService.create_promo(promoAmount=-1,description='',promoType='test',startTime="2021-01-12",endTime="2021-10-12",isActive=True,normalUserId=1,creatorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry promoAmount should be bigger than 0')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_create_promo_startTime_should_less_than_endTime(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        normalUserRepository.get_one_by_id.return_value =  NormalUser(username='test',pk =1,name='test',address='test',mobileNumber="01150")
        
        result = promoService.create_promo(promoAmount=10,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,normalUserId=1,creatorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry startTime should be less than endTime')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_create_promo_should_return_new_promo(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        normalUserRepository.get_one_by_id.return_value =  NormalUser(username='test',pk =1,name='test',address='test',mobileNumber="01150")
        promoRepository.create_promo.return_value = Promo(promoAmount=10,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoCode=5093,creationTime="2021-11-11")
        result = promoService.create_promo(promoAmount=10,description='',promoType='test',startTime="2021-01-12",endTime="2021-10-12",isActive=True,normalUserId=1,creatorType="administrator_user")
        self.assertEqual(result.get('data').promoAmount , 10)

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_create_promo_should_return_internal_error_if_promo_not_created(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        normalUserRepository.get_one_by_id.return_value =  NormalUser(username='test',pk =1,name='test',address='test',mobileNumber="01150")
        promoRepository.create_promo.return_value = False
        result = promoService.create_promo(promoAmount=10,description='',promoType='test',startTime="2021-01-12",endTime="2021-10-12",isActive=True,normalUserId=1,creatorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry internal error happen while create promotion')


    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_edit_promo_promo_should_be_existed(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =  False
        
        result = promoService.modify_promo(promoAmount=-1,description='',startTime="2021-01-12",endTime="2021-10-12",isActive=True,promoId=1,editorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry this promo user isn\'t existed')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_edit_promo_editorType_should_be_admin(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =  False
        
        result = promoService.modify_promo(promoAmount=-1,description='',startTime="2021-01-12",endTime="2021-10-12",isActive=True,promoId=1,editorType='test')
        self.assertEqual(result.get('error') , 'sorry you must be administrator_user to create promotion')


    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_edit_promo_promoAmount_should_be_more_thant_zero(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =   Promo(promoAmount=10,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoCode=5093,creationTime="2021-11-11")
        
        result = promoService.modify_promo(promoAmount=-1,description='',startTime="2021-01-12",endTime="2021-10-12",isActive=True,promoId=1,editorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry promoAmount should be bigger than 0')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_edit_promo_startTime_should_less_than_endTime(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =   Promo(promoAmount=10,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoCode=5093,creationTime="2021-11-11")
        
        result = promoService.modify_promo(promoAmount=1,description='',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoId=1,editorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry startTime should be less than endTime')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_edit_promo_should_return_updated_one(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =   Promo(promoAmount=10,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoCode=5093,creationTime="2021-11-11")
        promoRepository.update.return_value =   Promo(promoAmount=1,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoCode=5093,creationTime="2021-11-11")
        
        result = promoService.modify_promo(promoAmount=1,description='',startTime="2021-01-12",endTime="2021-10-12",isActive=True,promoId=1,editorType="administrator_user")
        self.assertEqual(result.get('data').promoAmount , 1)

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_delete_promo_return_error_when_promo_not_existed(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =   None

        result = promoService.delete_promo(promoId=1,editorType="administrator_user")
        self.assertEqual(result.get('error') , 'sorry this promo user isn\'t existed')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_delete_promo_editorType_should_be_admin(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =   None
        
        result = promoService.delete_promo(promoId=1,editorType="test")
        self.assertEqual(result.get('error') , 'sorry you must be administrator_user to create promotion')

    @mock.patch('Promo.Repositories.PromoRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_delete_promo_return_deleted_promo(self, promoRepository,normalUserRepository):
    
        promoService = PromoService(promoRepository,normalUserRepository)

        promoRepository.get_one_by_id.return_value =  Promo(promoAmount=1,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoCode=5093,creationTime="2021-11-11")
        promoRepository.delete.return_value =  Promo(promoAmount=1,description='',promoType='test',startTime="2022-01-12",endTime="2021-10-12",isActive=True,promoCode=5093,creationTime="2021-11-11")
        
        result = promoService.delete_promo(promoId=1,editorType="administrator_user")
        self.assertEqual(result.get('data').promoAmount , 1)
