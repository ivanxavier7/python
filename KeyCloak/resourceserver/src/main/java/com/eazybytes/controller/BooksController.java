package com.eazybytes.controller;

import com.eazybytes.model.Accounts;
import com.eazybytes.model.Books;
import com.eazybytes.model.Customer;
import com.eazybytes.repository.BooksRepository;
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
