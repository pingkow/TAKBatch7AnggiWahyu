//choose product di gabung jadi 1 dengan checkout

describe('Checkout', () => {
    beforeEach(() => {
        cy.visit("/");
    })

    it("Negative case not choose size dan color +  qty not avail success", () => {
        //login with command
        cy.login_command();
        cy.get(':nth-child(4) > .product-item-info > .product-item-photo > .product-image-container > .product-image-wrapper > .product-image-photo').click();
        cy.wait(5000);

        //verify error message when user not choose size and color
        cy.get('#product-addtocart-button > span').click();
        cy.get('.mage-error').should("be.visible").should("contain.text","This is a required field.");
        
        //user add to cart after choose size and color
        cy.get('#option-label-size-143-item-168').click();
        cy.get('#option-label-color-93-item-49').click();
        cy.get('#product-addtocart-button > span').click();

        //verify success add to cart
        cy.get('.message-success').should("contain.text","You added");
        cy.get('.counter-number').should('not.have.text', '0');

        //verify error qty not avail
        cy.get('.showcart').click();
        cy.wait(3000);
        cy.get('[class*="item-qty"]').clear().type("9999");
        cy.get('.update-cart-item').click();
        cy.get('.modal-title').should("be.visible").should("contain.text","Attention");
        cy.get('.modal-content').should("be.visible").should("contain.text","The requested qty is not available");
        cy.get('.action-primary > span').click();

        //user can delete item from cart
        cy.get('.showcart').click();
        cy.get('.product-item-details > .actions > .secondary > .action').click();
        cy.get('.modal-content').should("be.visible").should("contain.text","Are you sure you would like to remove this item from the shopping cart?");
        cy.get('.action-primary > span').click();

    });

    it("Positive case checkout success", () => {
        //login with command
        cy.login_command();
        cy.get(':nth-child(4) > .product-item-info > .product-item-photo > .product-image-container > .product-image-wrapper > .product-image-photo').click();
        cy.wait(5000);

        //verify error message when user not choose size and color
        cy.get('#product-addtocart-button > span').click();
        cy.get('.mage-error').should("be.visible").should("contain.text","This is a required field.");
        
        //user add to cart after choose size and color
        cy.get('#option-label-size-143-item-168').click();
        cy.get('#option-label-color-93-item-49').click();
        cy.get('#product-addtocart-button > span').click();

        //verify success add to cart
        cy.get('.message-success').should("contain.text","You added");
        cy.get('.counter-number').should('not.have.text', '0');

        //verify error qty not avail
        cy.get('.showcart').click();
        cy.wait(3000);
        cy.get('#top-cart-btn-checkout').click();
        cy.url().should("eq", "https://magento.softwaretestingboard.com/checkout/#shipping");

        // next co & verify url payment
        cy.get('.button > span').click();
        cy.url().should("eq", "https://magento.softwaretestingboard.com/checkout/#payment");

        // place order
        cy.get('.payment-method-content > :nth-child(4) > div.primary > .action > span').click();

        //verify success
        cy.url().should("eq", "https://magento.softwaretestingboard.com/checkout/onepage/success/");
        cy.get('.checkout-success > :nth-child(2)').should("contain.text","We'll email you an order confirmation with details and tracking info.");
  
    });

  
  });