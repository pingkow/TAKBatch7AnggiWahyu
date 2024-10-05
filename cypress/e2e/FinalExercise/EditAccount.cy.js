describe('EditAccountMagento', () => {
    beforeEach(() => {
        cy.visit("/");
    })

    it("Positive case EditAccount success", () => {
        //login with command
        cy.login_command();

        //negative case edit account
        cy.get(':nth-child(2) > .customer-welcome > .customer-name > .action').click();
        cy.get(':nth-child(2) > .customer-welcome > .customer-menu > .header > :nth-child(1) > a').click();

        //verify url account page
        cy.url().should("eq", "https://magento.softwaretestingboard.com/customer/account/");
        cy.get('.block-dashboard-info > .block-content > .box > .box-actions > .edit > span').click();
        //verify url edit account page
        cy.url().should("eq", "https://magento.softwaretestingboard.com/customer/account/edit/");

        cy.get('#firstname').clear().type("Wahyu Edit");
        cy.get('#lastname').clear().type("TAK Edit");
        cy.get('#form-validate > .actions-toolbar > div.primary > .action > span').click();
        cy.wait(10000);

        //verify sudah di edit
        cy.get(':nth-child(2) > .greet > .logged-in').should("contain.text","Edit")

        //ini saya edit lagi ke awal ya kak
        cy.get('.block-dashboard-info > .block-content > .box > .box-actions > .edit > span').click();
        cy.get('#firstname').clear().type("Wahyu");
        cy.get('#lastname').clear().type("TAK");
        cy.get('#form-validate > .actions-toolbar > div.primary > .action > span').click();

    });

    it("Negative case EditAccount blank field", () => {
        //login with command
        cy.login_command();

        //negative case edit account
        cy.get(':nth-child(2) > .customer-welcome > .customer-name > .action').click();
        cy.get(':nth-child(2) > .customer-welcome > .customer-menu > .header > :nth-child(1) > a').click();

        //verify url account page
        cy.url().should("eq", "https://magento.softwaretestingboard.com/customer/account/");
        cy.get('.block-dashboard-info > .block-content > .box > .box-actions > .edit > span').click();
        //verify url edit account page
        cy.url().should("eq", "https://magento.softwaretestingboard.com/customer/account/edit/");

        cy.get('#firstname').clear();
        cy.get('#lastname').clear();
        cy.get('#form-validate > .actions-toolbar > div.primary > .action > span').click();

        //verify error message
        cy.get('#firstname-error').should("be.visible").should("contain.text","This is a required field.");
        cy.get('#lastname-error').should("be.visible").should("contain.text","This is a required field.");
    });

  
  });