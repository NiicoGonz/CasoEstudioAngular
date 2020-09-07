import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ClientService } from '../client.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-bill',
  templateUrl: './bill.component.html',
  styleUrls: ['./bill.component.css']
})
export class BillComponent implements OnInit {
  form: FormGroup;
  // tslint:disable-next-line: variable-name
  img_background = './assets/background.jpg';
  // tslint:disable-next-line: variable-name
  img_circle = './assets/register-fac.png';
  identificationCard: string;
  lastname: string;
  line: string;
  name: string;
  datebill: string;
  // tslint:disable-next-line: variable-name
  id_fac: string;
  valuefac: string;

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router
    ){}
  ngOnInit(): void {
  this.form = this.fb.group({
    mobileline: ['', Validators.required],
    date: ['', Validators.required]
  });
  }

 // tslint:disable-next-line: typedef
 async onSubmit(){
   if (this.form.valid){
     this.client
       .getRequest(
         `http://localhost:5000/api/v01/bill/get/${this.form.value.mobileline}`,
         localStorage.getItem('token')
       )
       .subscribe((Response: any) => {
         // console.log(Response);
         const {usuario} = Response;
         const {identificationCard, lastname, line, name } = usuario;
         const {factura} = Response;
         const {date, id_fac, value} = factura;
         this.id_fac = id_fac;
         this.datebill = date;
         this.valuefac = value;
         this.identificationCard = identificationCard;
         this.lastname = lastname;
         this.line = line;
         this.name = name;
        }),
       // tslint:disable-next-line: no-unused-expression
       (error) => {
         console.log(error.status);
       };
   }else{
     console.log('error en el ingreso de datos');
   }
 }

}
