"""CreateAccountsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAccountsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("accounts") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("accounts")
