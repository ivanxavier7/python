package com.group_2.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "books")
public class Books {
    @Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Column(name = "book_id")
	private int bookId;

    @Column(name = "name")
	private String name;

    @Column(name = "description")
	private String description;

    @Column(name = "author")
	private String author;

    @Column(name = "price")
	private int price;

    @Column(name = "email")
	private String email;

    public int getId(){
        return bookId;
    }

    public void setId(int id){
        this.bookId = id;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getDescription(){
        return description;
    }

    public void setDescription(String description){
        this.description = description;
    }

    public String getAuthor(){
        return author;
    }

    public void setAuthor(String author){
        this.author = author;
    }

    public int getPrice(){
        return price;
    }

    public void setPrice(int price){
        this.price = price;
    }

    public String getAccountId(){
        return email;
    }

    public void setAccountId(String email){
        this.email = email;
    }
}
