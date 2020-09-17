import { Component, OnInit } from '@angular/core';
import { ClientService } from '../client.service';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {  Router} from '@angular/router';

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css']
})
export class CustomerComponent implements OnInit {

  form: FormGroup;
  // Inyeccion de depencias
  constructor(private fb: FormBuilder, private client: ClientService, private route: Router ){}

  // tslint:disable-next-line: ban-types
  // tslint:disable-next-line: no-inferrable-types
  notification: boolean;
  // tslint:disable-next-line: variable-name
  img_background = './assets/background.jpg';
  // tslint:disable-next-line: variable-name
  img_circle = './assets/register-person.png';


  ngOnInit(): void {
    if (!localStorage.getItem('token')){
      this.route.navigate(['/']);
    }

    this.form = this.fb.group({
      name : ['', Validators.required],
      lastname : [ '', Validators.required],
      identificationCard : [ '', Validators.required],
      phone : [ '', Validators.required],
      dateBorn : [ '', Validators.required]
    });
  }
  // tslint:disable-next-line: typedef
  async onSubmit(){
    // Se recupera el token
    if (this.form.valid){
      this.client.postRequest(
        'http://localhost:5000/api/v01/customer/register',
        {
          name : this.form.value.name,
          lastname : this.form.value.lastname,
          identificationCard : this.form.value.identificationCard,
          phone : this.form.value.phone,
          dateBorn : this.form.value.dateBorn
        },
        // Se envia el token
        localStorage.getItem('token')
      ).subscribe(
        (response: any) => {
          // console.log(response);
          this.form.reset();

        }
      ),
      // tslint:disable-next-line: no-unused-expression
      (error) => {
        console.log(error.status);

      };
    }else{
      console.log('Error en la entrada de datos del formulario del cliente');
      this.notification = true;

    }

  }

}
