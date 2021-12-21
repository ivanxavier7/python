package com.uap.controller;

import com.uap.model.Books;
import com.uap.model.Customer;
import com.uap.repository.BooksRepository;
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
        List<Books> books = booksRepository.findByCustomerId(customer.getId());
        if(books != null){
            return books;
        } else {
            return null;
        }
    }
}
