import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  constructor(private route: Router) { }
  welcome(){
    this.route.navigate([''])
  }

  login(){
    this.route.navigate(['login'])
  }


  registerConsultant(){
    this.route.navigate(['/registerConsultant'])
  }

  registerCustomer(){
    this.route.navigate(['/registerCustomer'])
  }

  registerEquipment(){
    this.route.navigate(['/registerEquipment'])
  }

  line(){
    this.route.navigate(['/line'])
  }

  consultantBill(){
    this.route.navigate(['/consultantBill'])
  }


  token = '';
  userInSystem  = false;
  
  ngOnInit(): void {
    this.token = localStorage.getItem('token');
    if(this.token){
      this.userInSystem = true;
    }else{
      this.userInSystem = false;
    }
  } 

}
