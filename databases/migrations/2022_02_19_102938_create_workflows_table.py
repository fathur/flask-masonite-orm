"""CreateWorkflowsTable Migration."""

from masoniteorm.migrations import Migration


class CreateWorkflowsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("workflows") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("workflows")
