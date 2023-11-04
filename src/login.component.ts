import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  rememberLogin: boolean = false;

  login() {
    // Implement your login logic here
    console.log('Username:', this.username);
    console.log('Password:', this.password);
    console.log('Remember Login:', this.rememberLogin);

    // You can add your authentication logic and routing to other pages here
  }
}
