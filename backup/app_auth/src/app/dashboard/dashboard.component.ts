import { Component, OnInit } from '@angular/core';
import {User} from "../user.model";

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  user = new User();

  constructor() { }

  ngOnInit(): void {

    this.user = JSON.parse(<string>sessionStorage.getItem('userdetails'));
    console.log(this.user);
  }

}
