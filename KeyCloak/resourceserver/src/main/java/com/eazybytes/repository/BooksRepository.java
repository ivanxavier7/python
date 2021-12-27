package com.eazybytes.repository;

import com.eazybytes.model.Books;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BooksRepository extends CrudRepository<Books, Long> {
    List<Books> findByEmail(String email);
}
