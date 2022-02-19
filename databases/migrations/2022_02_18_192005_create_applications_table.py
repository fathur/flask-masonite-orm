"""CreateApplicationsTable Migration."""

from masoniteorm.migrations import Migration


class CreateApplicationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("applications") as table:
            table.big_increments("id")
            table.big_integer('user_id').unsigned()
            table.date('birth_at')
            table.enum('gender', ['M', 'F'])
            table.string('identity_number', 16).nullable().unique()
            table.string('address_street')
            table.unsigned_integer('region_id').nullable()
            table.unsigned_integer('status_id').default(0)

            table.foreign('user_id').references('id').on('users')
            table.foreign('region_id').references('id').on('regions')
            table.foreign('status_id').references('id').on('statuses')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("applications")
