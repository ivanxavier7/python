package com.uap.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.authentication.www.BasicAuthenticationFilter;
import org.springframework.security.web.csrf.CookieCsrfTokenRepository;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;

import com.uap.filter.AuthoritiesLoggingAfterFilter;
import com.uap.filter.AuthoritiesLoggingAtFilter;
import com.uap.filter.JWTTokenGeneratorFilter;
import com.uap.filter.JWTTokenValidatorFilter;
import com.uap.filter.RequestValidationBeforeFilter;

import javax.servlet.http.HttpServletRequest;

import java.util.Arrays;
import java.util.Collections;

@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true,securedEnabled = true, jsr250Enabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {

        http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS).and()
        .cors().configurationSource(new CorsConfigurationSource() {
                    @Override
                    public CorsConfiguration getCorsConfiguration(HttpServletRequest request) {
                        CorsConfiguration config = new CorsConfiguration();
                        config.setAllowedOrigins(Collections.singletonList("http://localhost:4200"));
                        config.setAllowedMethods(Collections.singletonList("*"));
                        config.setAllowCredentials(true);
                        config.setAllowedHeaders(Collections.singletonList("*"));
                        config.setExposedHeaders(Arrays.asList("Authorization"));
                        config.setMaxAge(3600L);
                        return config;
                    }
                }).and().csrf().disable()
						.addFilterBefore(new RequestValidationBeforeFilter(), BasicAuthenticationFilter.class)
						.addFilterAfter(new AuthoritiesLoggingAfterFilter(), BasicAuthenticationFilter.class)
						.addFilterBefore(new JWTTokenValidatorFilter(), BasicAuthenticationFilter.class)
						.addFilterAfter(new JWTTokenGeneratorFilter(), BasicAuthenticationFilter.class)
						.addFilterAt(new AuthoritiesLoggingAtFilter(), BasicAuthenticationFilter.class)
		                .authorizeRequests()
		                .antMatchers("/myAccount").hasRole("USER")
		                .antMatchers("/myBooks").hasRole("ADMIN")
		                .antMatchers("/myCards").authenticated()
		                .antMatchers("/contact").permitAll().and().httpBasic();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
