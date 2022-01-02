# SIO - Project 2 - Authentication - UAP

-----

## Instructions to run the project - UAP

To run the UAP, make sure you have [JDK 1.8](https://www.oracle.com/java/technologies/downloads/) or later, [Maven](https://maven.apache.org/install.html) or [Gradle 4+](https://gradle.org/install/) installed
- **1º:** In you terminal, enter in the folder **keycloak-16/bin/** and run **bash standalone.sh** or simply type **keycloak-16/bin/./standalone.sh**
- **2º:** Enter in the folder uap/uap and run spring boot using one of the following options: <br>
   - ./mvnw spring-boot:run <br>
      or <br>
   -  mvn spring-boot:run <br>
   
      if you have gradle installed <br>
   -  ./gradlew bootRun 
- **3º:** Finally follows instructions in [app_auth](https://github.com/detiuaveiro/project-2---authentication-equipa_2/tree/master/app_auth) to run it

## References
**[1]** -  [PKCE](https://www.oauth.com/oauth2-servers/pkce/) <br>
**[2]** -  [OAUTH 2.0](https://oauth.net/2/) <br>
**[3]** -  [CODE VERIFIER - CODE CHALLENGE](https://datatracker.ietf.org/doc/html/rfc7636#page-8) <br>
**[4]** -  [KEYCLOAK](https://www.keycloak.org/) <br>








