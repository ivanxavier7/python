import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {LoginComponent} from "./login/login.component";
import {DashboardComponent} from "./dashboard/dashboard.component";
import {ContactComponent} from "./contact/contact.component";
import {BooksComponent} from "./books/books.component";
import {AuthKeyClockGuard} from "./appAuthGuard";
import {AccountComponent} from "./account/account.component";

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full'},
  { path: 'login', component: LoginComponent},
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthKeyClockGuard], data: {roles: ['USER', 'ADMIN']}},
  { path: 'books', component: BooksComponent},
  { path: 'contact', component: ContactComponent},
  { path: 'account', component: AccountComponent, canActivate: [AuthKeyClockGuard],data: {roles: ['USER']}},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
