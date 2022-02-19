"""CreateStatusesTable Migration."""

from masoniteorm.migrations import Migration


class CreateStatusesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("statuses") as table:
            table.unsigned_integer("id")
            table.string('name')
            table.timestamps()

            table.primary("id")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("statuses")
