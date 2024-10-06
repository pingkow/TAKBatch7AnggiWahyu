describe('LoginAccountMagento', () => {
    beforeEach(() => {
        cy.visit("/");
    })

    it("Negative Login blank field", () => {
        //Masuk ke page create account
        cy.get('.panel > .header > .authorization-link > a').click();
        cy.wait(5000);

        //verify URL
        cy.url().should("contain", "/login");
        cy.get('.login-container > .block-customer-login > .block-content > #login-form > .fieldset > .actions-toolbar > div.primary > #send2 > span').click();
        cy.get('#email-error').should("be.visible").should("contain.text","This is a required field.");
        cy.get('#pass-error').should("be.visible").should("contain.text","This is a required field.");

    });

    it("Negative Login wrong password", () => {
        //Masuk ke page create account
        cy.get('.panel > .header > .authorization-link > a').click();
        cy.wait(5000);

        cy.get('#email').type("wahyutak@gmail.com");
        cy.get('.login-container > .block-customer-login > .block-content > #login-form > .fieldset > .password > .control > #pass').type("wrongpass");
        cy.get('.login-container > .block-customer-login > .block-content > #login-form > .fieldset > .actions-toolbar > div.primary > #send2 > span').click();
        cy.get('.message-error > div').should("be.visible").should("contain.text","The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.");

    });

    it("Positive Login Success", () => {
        //Masuk ke page create account
        cy.get('.panel > .header > .authorization-link > a').click();
        cy.wait(5000);

        cy.get('#email').type("wahyutak@gmail.com");
        cy.get('.login-container > .block-customer-login > .block-content > #login-form > .fieldset > .password > .control > #pass').type("Takbatch7");
        cy.get('.login-container > .block-customer-login > .block-content > #login-form > .fieldset > .actions-toolbar > div.primary > #send2 > span').click();
        cy.wait(10000);
        cy.get(':nth-child(2) > .greet > .logged-in').should("be.visible").should("contain.text","Welcome");

    });

  
  });