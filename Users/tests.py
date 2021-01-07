from django.test import TestCase
import mock
from Users.Services.UserServices import UsersService
from Users.Repositories.AdministratorUserRepository import AdministratorUserRepository
from Users.Repositories.NormalUserRepository import NormalUserRepository
from Users.models import AdministratorUser , NormalUser


class UserServiceAdministratorUserLoginTest(TestCase):
    
    @mock.patch('Users.Repositories.AdministratorUserRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_administrator_user_login_should_return_error(self, administratorUserRepository,normalUserRepository):
    
        usersService = UsersService(administratorUserRepository,normalUserRepository)

        administratorUserRepository.get_one_by_user_name.return_value = False
        
        result = usersService.administrator_user_login('test')
        self.assertEqual(result.get('error') , 'sorry this user isn\'t exists')

    @mock.patch('Users.Repositories.AdministratorUserRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_administrator_user_login_should_return_user_data(self, administratorUserRepository,normalUserRepository):
    
        usersService = UsersService(administratorUserRepository,normalUserRepository)

        administratorUserRepository.get_one_by_user_name.return_value = AdministratorUser(username='test',pk =1,name='test',address='test')
        
        result = usersService.administrator_user_login('test')
        
        self.assertEqual(result.get('data').get('userName') , 'test')
        self.assertEqual(result.get('data').get('id') , 1)




class UserServiceNormalUserLoginTest(TestCase):
    
    @mock.patch('Users.Repositories.AdministratorUserRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_normal_user_login_should_return_error(self, administratorUserRepository,normalUserRepository):
    
        usersService = UsersService(administratorUserRepository,normalUserRepository)

        normalUserRepository.get_one_by_user_name.return_value = False
        
        result = usersService.normal_user_login('test')
        self.assertEqual(result.get('error') , 'sorry this user isn\'t exists')

    @mock.patch('Users.Repositories.AdministratorUserRepository')
    @mock.patch('Users.Repositories.NormalUserRepository')
    def test_normal_user_login_should_return_user_data(self, administratorUserRepository,normalUserRepository):
    
        usersService = UsersService(administratorUserRepository,normalUserRepository)

        normalUserRepository.get_one_by_user_name.return_value = NormalUser(username='test',pk =1,name='test',address='test',mobileNumber="01150")
        
        result = usersService.normal_user_login('test')
        
        self.assertEqual(result.get('data').get('userName') , 'test')
        self.assertEqual(result.get('data').get('id') , 1)

