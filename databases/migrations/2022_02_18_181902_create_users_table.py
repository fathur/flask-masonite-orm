"""MigrationForUsersTable Migration."""

from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.big_increments("id")
            table.string('password')
            table.string('email').nullable().unique()
            table.string('identity_number', 16).nullable().unique()
            table.string('phone').nullable().unique()
            table.string('first_name')
            table.string('last_name').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
