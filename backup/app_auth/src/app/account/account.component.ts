import { Component, OnInit } from '@angular/core';
import {User} from "../user.model";
import {Account} from "../account.model";
import {DashboardService} from "../dashboard.service";

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
  user = new User();
  account = new Account();
  constructor(private dashboardService: DashboardService) { }

  ngOnInit(): void {
    this.user = JSON.parse(<string>sessionStorage.getItem('userdetails'));
    if(this.user){
      this.dashboardService.getAccountDetails(this.user).subscribe(
        responseData => {
          this.account = <any> responseData.body;
        }, error => {
          console.log(error);
        });
    }
  }

}
