import { Component, OnInit } from '@angular/core';
import { ClientService } from '../client.service';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {  Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent{

  form: FormGroup;
  // Inyeccion de dependencias
  constructor(private fb: FormBuilder, private client: ClientService,  private route: Router){}

  // tslint:disable-next-line: variable-name
  img_background = './assets/background.jpg';
  // tslint:disable-next-line: variable-name
  img_circle = './assets/user.png';

  // tslint:disable-next-line: use-lifecycle-interface
  ngOnInit(): void {
    this.form = this.fb.group({
      email : ['', Validators.email],
      password : [ '', Validators.required]
    });
  }

  // tslint:disable-next-line: typedef
  async onSubmit(){
    if (this.form.valid){
      this.client
        .postRequest(' http://localhost:5000/api/v01/login', {
          email: this.form.value.email,
          password: this.form.value.password,
        })
        .subscribe((response: any) => {
          console.log(response);
          localStorage.setItem('token', response.token);
          this.route.navigate(['/']);
        }),
        // tslint:disable-next-line: no-unused-expression
        (error) => {
          console.log(error.status);
        };


    }else{
     console.log('Error en la entrada de datos del formulario del cliente');
    }

  }

}
