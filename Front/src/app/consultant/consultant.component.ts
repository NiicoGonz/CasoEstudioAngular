import { Component, OnInit } from '@angular/core';
import { ClientService } from '../client.service';
// tslint:disable-next-line: import-spacing
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {  Router} from '@angular/router';

@Component({
  selector: 'app-consultant',
  templateUrl: './consultant.component.html',
  styleUrls: ['./consultant.component.css']
})
export class ConsultantComponent implements OnInit {

  form: FormGroup;
  // Inyeccion de dependencias
  constructor(private fb: FormBuilder, private client: ClientService,  private route: Router){

  }

  // tslint:disable-next-line: variable-name
  img_background = './assets/background.jpg';
  // tslint:disable-next-line: variable-name
  img_circle = './assets/register-person.png';

  ngOnInit(): void {
  this.form = this.fb.group({
    name : ['', Validators.required],
    lastname : ['', Validators.required],
    id : ['', Validators.required],
    phonenumber : ['', Validators.required],
    address : ['', Validators.required],
    email : ['', Validators.email],
    password : [ '', Validators.required],
    rol : ['', Validators.required]

  });
  }

  // tslint:disable-next-line: typedef
  async onSubmit(){
    if (this.form.valid){

      this.client.postRequest('http://localhost:5000/api/v01/consultant/register' , {
        name : this.form.value.name,
        lastname : this.form.value.lastname,
        identificationCard : this.form.value.id,
        phone : this.form.value.phonenumber,
        address : this.form.value.address,
        email : this.form.value.email,
        password : this.form.value.password,
        rol : this.form.value.rol[0]
      }).subscribe(
        (response: any) => {
            this.route.navigate (['/login']);
        }
      );
    }else{
      console.log('Error en la validacion del form');

    }
  }

}
