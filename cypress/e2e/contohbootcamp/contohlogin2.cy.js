describe('Test Login OrangeHRM', () => {
  beforeEach(() => {
    cy.visit('https://bstackdemo.com/signin')
  })

  it('test login failed', () => {
    cy.get('#login-btn').click();
    cy.get(".api-error").should("be.visible")
    cy.get(".api-error").should("contain.text","Invalid Username");
  });

  it('test login success dropdown', () => {
    cy.get('#username > .css-yk16xz-control > .css-1hwfws3').should("have.text","Select Username");
    cy.get('#username > .css-yk16xz-control > .css-1hwfws3').click();
    cy.get('#react-select-2-option-0-0').click();
    cy.get('#password > .css-yk16xz-control > .css-1hwfws3').should("have.text","Select Password");
    cy.get('#password > .css-yk16xz-control > .css-1hwfws3').click();
    cy.get('#react-select-3-option-0-0').click();
    cy.get('#login-btn').click();
    cy.url().should("include", "https://bstackdemo.com/?signin=true");
    cy.get('.username').should("contain.text","demouser")
  });

  
  it('test login success type', () => {
    cy.get('#username > .css-yk16xz-control > .css-1hwfws3').should("have.text","Select Username");
    cy.get('#username > .css-yk16xz-control > .css-1hwfws3').type("fav_user{enter}");
    cy.get('#password > .css-yk16xz-control > .css-1hwfws3').should("have.text","Select Password");
    cy.get('#password > .css-yk16xz-control > .css-1hwfws3').type("testingisfun99{enter}");
    cy.get('#login-btn').click();
    cy.url().should("include", "https://bstackdemo.com/?signin=true");
    cy.get('.username').should("contain.text","fav_user")
  });



});