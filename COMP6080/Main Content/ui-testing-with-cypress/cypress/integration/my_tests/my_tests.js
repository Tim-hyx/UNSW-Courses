context('Signup flow - happy path', () => {
  beforeEach(() => {
    cy.visit('localhost:3000');
  });

  it('Successfully signs up', () => {
    const name = 'Jane Doe';
    const email = 'jane.doe@example.com';
    const password = 'passw0rd';

    cy.get('input[name=name]')
      .focus()
      .type(name);
    
    cy.get('input[name=email]')
      .focus()
      .type(email);

    cy.get('input[name=password]')
      .focus()
      .type(password);

    cy.get('button[type=submit]')
      .click()

    cy.get('[data-test-target=CaptionText]').then(el => {
      expect(el.text()).to.contain(email);
    });
  });
});
