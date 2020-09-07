import { Component, OnInit } from '@angular/core';
import { ClientService } from '../client.service';
// tslint:disable-next-line: import-spacing
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {  Router} from '@angular/router';

@Component({
  selector: 'app-equipment',
  templateUrl: './equipment.component.html',
  styleUrls: ['./equipment.component.css']
})
export class EquipmentComponent implements OnInit {

  form: FormGroup;

  estados = [
    {value : '0' , description : 'Selected'},
    {value : '1' , description : 'Reported'},
    {value : '2' , description : 'Not Reported'},
  ];

  constructor(private fb: FormBuilder, private client: ClientService,  private route: Router){}

  // tslint:disable-next-line: variable-name
  img_circle = './assets/register-mobile.png';

  ngOnInit(): void {
    this.form = this.fb.group({
      lineNumber : ['', Validators.required],
      serial : [ '', Validators.required],
      imei : [ '', Validators.required],
      trademark : [ '', Validators.required],
      state : [ '', Validators.required],
    });
  }

  // tslint:disable-next-line: typedef
  async onSubmit(){
    if (this.form.valid){
      this.client
        .postRequest(
          'http://localhost:5000/api/v01/equipment/register',
          {
            lineNumber: this.form.value.lineNumber,
            serial: this.form.value.serial,
            imei: this.form.value.imei,
            trademark: this.form.value.trademark,
            state: this.form.value.state,
          },
          localStorage.getItem('token')
        )
        .subscribe((response: any) => {
          console.log(response);
          this.form.reset();
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
