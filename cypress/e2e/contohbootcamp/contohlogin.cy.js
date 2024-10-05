const cypressConfig = require("../../../cypress.config");

describe('Test Login OrangeHRM', () => {
  beforeEach(() => {
    cy.visit(cypress.config("baseUrl"));
  })

  it('test login failed', () => {
    cy.get('[name=username]').type("Wrongadmin")
    cy.get('[name=password]').type("wrongpass");
    cy.get(".oxd-button").click()
    cy.get(".oxd-alert-content > .oxd-text").should("contain.text","Invalid credentials");
  });

  it('test login success', () => {
    cy.get('[name=username]').type("Admin")
    cy.get('[name=password]').type("admin123");
    cy.get(".oxd-button").click()
    cy.get(".oxd-userdropdown-name").should("be.visible")
    cy.url().should("include", "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index");

  });
 


});