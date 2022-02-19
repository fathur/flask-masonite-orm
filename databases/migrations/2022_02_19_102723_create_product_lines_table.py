"""CreateProductLinesTable Migration."""

from masoniteorm.migrations import Migration


class CreateProductLinesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("product_lines") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("product_lines")
