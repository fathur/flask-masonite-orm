"""CreateRegionsTable Migration."""

from masoniteorm.migrations import Migration


class CreateRegionsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("regions") as table:
            table.increments("id")
            table.string('name')
            table.unsigned_integer('_lft').nullable()
            table.unsigned_integer('_rgt').nullable()
            table.unsigned_integer('_lvl').nullable()
            table.string('postal_code').nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("regions")
