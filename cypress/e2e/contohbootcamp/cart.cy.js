describe('Test add to cart BstackDemo', () => {
    beforeEach(() => {
        cy.visit("/");
        cy.get("#username").should("have.text","Select Username").type("fav_user{enter}");
        cy.get("#password").should("have.text","Select Password").type("testingisfun99{enter}");
        cy.get("#login-btn").click();
        cy.get(".username").should("be.visible").should("contain","fav_user")

    })
  
    it("success add to cart 1 product", () => {
      cy.get("#1").should("be.visible");
      cy.get("#1").children(".shelf-item__buy-btn").click();  
      cy.get('.bag__quantity').should("have.text","1");

    //checkout
      cy.get('.buy-btn').click();
      cy.url().should("include", "/checkout");
    });
  

   
  
  
  });