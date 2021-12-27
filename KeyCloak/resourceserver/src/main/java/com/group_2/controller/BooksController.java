package com.group_2.controller;

import com.group_2.model.Books;
import com.group_2.model.Customer;
import com.group_2.repository.BooksRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class BooksController {

    @Autowired
    private BooksRepository booksRepository;

    @PostMapping("/myBooks")
    public List<Books> getBookDetails(@RequestBody Customer customer){
        List<Books> books = booksRepository.findByEmail(customer.getEmail());
        if(books != null){
            return books;
        } else {
            return null;
        }
    }
}
