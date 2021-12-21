package com.uap.uap_rest_api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.ComponentScans;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;

@SpringBootApplication
@ComponentScans({ @ComponentScan("com.uap.controller"), @ComponentScan("com.uap.config")})
@EnableJpaRepositories("com.uap.repository")
@EntityScan("com.uap.model")
public class UapRestApiApplication {

	public static void main(String[] args) {
		SpringApplication.run(UapRestApiApplication.class, args);
	}

}
