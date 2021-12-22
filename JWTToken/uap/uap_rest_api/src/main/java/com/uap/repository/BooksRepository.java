package com.uap.repository;

import com.uap.model.Books;
import org.springframework.data.repository.CrudRepository;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BooksRepository extends CrudRepository<Books, Long> {

    @PreAuthorize("hasRole('USER')")
    List<Books> findByCustomerId(int customerId);
}
