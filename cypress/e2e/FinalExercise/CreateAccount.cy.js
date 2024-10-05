describe('CreateAccountMagento', () => {
    beforeEach(() => {
        cy.visit("/");
    })
  
    it("Negative Case Create account blank field", () => {
        //Masuk ke page create account
        cy.get('.panel > .header > :nth-child(3) > a').click();

        //verify URL
        cy.url().should("eq", "https://magento.softwaretestingboard.com/customer/account/create/");
        cy.get('#form-validate > .actions-toolbar > div.primary > .action > span').click();
 
        //Verify Error Message
        cy.get('#firstname-error').should("be.visible").should("contain.text","This is a required field.");
        cy.get('#lastname-error').should("be.visible").should("contain.text","This is a required field.");
        cy.get('#email_address-error').should("be.visible").should("contain.text","This is a required field.");
        cy.get('#password-error').should("be.visible").should("contain.text","This is a required field.");
        cy.get('#password-error').should("be.visible").should("contain.text","This is a required field.");
    });
  
    it("Negative Case Create account wrong email format", () => {
        //Masuk ke page create account
        cy.get('.panel > .header > :nth-child(3) > a').click();
        
        //Verify Error Message
        cy.get('#email_address').type("emailsalah");
        cy.get('#form-validate > .actions-toolbar > div.primary > .action > span').click();
        cy.get('#email_address-error').should("be.visible").should("contain.text","Please enter a valid email address (Ex: johndoe@domain.com).");
    });

    it("Negative Case Create account Confirm password not match", () => {
        //Masuk ke page create account
        cy.get('.panel > .header > :nth-child(3) > a').click();
        
        //Verify Error Message
        cy.get('#password').type("Password123");
        cy.get('#password-confirmation').type("passwordbeda");
        cy.get('#form-validate > .actions-toolbar > div.primary > .action > span').click();
        cy.get('#password-confirmation-error').should("be.visible").should("contain.text","Please enter the same value again.");
    });

    it("Positive Case Create account Success", () => {
        
        cy.get('.panel > .header > :nth-child(3) > a').click();
        cy.get('#firstname').type("Wahyu");
        cy.get('#lastname').type("Saputra");
        cy.get('#email_address').type("Wahyusaputra1@mailo.co")
        cy.get('#password').type("Password123")
        cy.get('#password-confirmation').type("Password123")
        cy.get('#form-validate > .actions-toolbar > div.primary > .action > span').click();

        //verify success
        cy.url().should("eq", "https://magento.softwaretestingboard.com/customer/account/");
        cy.get('.message-success > div').should("be.visible").should("contain.text","Thank you for registering with Main Website Store.");

    });
   
  
  
  });