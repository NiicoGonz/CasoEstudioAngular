import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { WelcomeComponent } from './welcome/welcome.component';
import { LoginComponent } from './login/login.component';
import { ConsultantComponent } from './consultant/consultant.component';
import { CustomerComponent } from './customer/customer.component';
import { EquipmentComponent } from './equipment/equipment.component';
import { LineComponent } from './line/line.component';
import { BillComponent } from './bill/bill.component';



const routes: Routes = [
  {path: '', component: WelcomeComponent},
  {path: 'login', component: LoginComponent},
  {path: 'registerConsultant', component: ConsultantComponent},
  {path: 'registerCustomer', component: CustomerComponent},
  {path: 'registerLine', component: LoginComponent},
  {path: 'updateLine', component: LoginComponent},
  {path: 'consultantLine', component: LoginComponent},
  {path: 'registerEquipment', component: EquipmentComponent},
  {path: 'line', component: LineComponent},
  {path: 'consultantBill', component: BillComponent},
  {path: 'deleteBill', component: BillComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
