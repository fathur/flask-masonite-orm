"""CreateDevicesTable Migration."""

from masoniteorm.migrations import Migration


class CreateDevicesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("devices") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("devices")
