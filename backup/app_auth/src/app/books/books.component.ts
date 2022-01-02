import { Component, OnInit } from '@angular/core';
import {DashboardService} from "../dashboard.service";
import {User} from "../user.model";

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {
  user = new User()
  books = new Array()
  constructor(private dashboardService: DashboardService) { }

  ngOnInit(): void {
    this.user = JSON.parse(<string>sessionStorage.getItem('userdetails'));
    if(this.user){
      this.dashboardService.getBooksDetails(this.user).subscribe(
        responseData => {
          this.books = <any> responseData.body;
        }, error => {
          console.log(error);
        });
    }
  }
}
