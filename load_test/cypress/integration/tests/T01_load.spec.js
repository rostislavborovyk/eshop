describe('Anonymous user tests', () => {
  it('Get all products pages', () => {
    cy.visit("http://localhost:8000/products");
    cy.get("a[class=product-link]")
      .each(($el, index, $list) => {
        cy.get("a[class=product-link]").eq(index).click();
        cy.get("div[class=product__inner-container]").first()
          .get("h1").should("be.visible");
        cy.go("back");
      });
  })
})