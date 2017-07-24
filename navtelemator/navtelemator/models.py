from django.core.urlresolvers import reverse
from django.db import models


class Cable(models.Model):
    id = models.AutoField(db_column='id')  # Field name made lowercase.
    name = models.CharField(db_column='cable', max_length=30, primary_key=True)
    end_a = models.ForeignKey('End', db_column='end_a')  # Field name made lowercase.
    end_b = models.ForeignKey('End', db_column='end_b')  # Field name made lowercase.
    owner = models.ForeignKey('Owner', db_column='owner', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cable'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cable-info', args=[str(self.name)])


class Circuit(models.Model):
    id = models.AutoField(db_column='id')
    name = models.CharField(db_column='circuit', max_length=30, primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='speed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='alias', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'circuit'

    def __unicode__(self):
        return self.name

    def get_circuits_by_end(end):
        circuitends = CircuitEnd.objects.filter(end=end)
        circuits = Circuit.objects.filter(circuitends.values('circuit'))
        return circuits

    def get_absolute_url(self):
        return reverse('circuit-info', args=[str(self.name)])


class CircuitDetail(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    circuit = models.ForeignKey('Circuit', db_column='circuit')
    index = models.IntegerField(db_column='index')
    end = models.ForeignKey('End', db_column='end')

    class Meta:
        managed = False
        db_table = 'circuit_detail'

    def __unicode__(self):
        return str(self.index + 1) + self.end


class CircuitEnd(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    circuit = models.ForeignKey('Circuit', db_column='circuit')  # Field name made lowercase.
    parallel = models.IntegerField(db_column='parallel')  # Field name made lowercase.
    end = models.ForeignKey('End', db_column='end')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'circuit_end'
        unique_together = (('circuit', 'parallel'),)

    def __unicode__(self):
        if self.parallel == 1:
            return self.circuit + ' Start'
        elif self.parallel == 2:
            return self.circuit + ' Stop'
        else:
            return self.circuit + ' Unknown'


class Connection(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    port = models.ForeignKey('Port', db_column='port')  # Field name made lowercase.
    pin = models.DecimalField(db_column='pin', max_digits=2, decimal_places=0)  # Field name made lowercase.
    circuit = models.ForeignKey('Circuit', db_column='circuit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'connection'
        unique_together = (('port', 'pin'),)

    def __unicode__(self):
        return u'Port %s Pin %s' % (self.port, self.pin)


class End(models.Model):
    id = models.AutoField(db_column='id')
    name = models.CharField(db_column='end', max_length=30, primary_key=True)  # Field name made lowercase.
    room = models.ForeignKey('End', db_column='room', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'end'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room-info', args=[str(self.name)])


class Owner(models.Model):
    id = models.AutoField(db_column='id')  # Field name made lowercase.
    owner = models.CharField(db_column='owner', max_length=10, primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='email', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'owner'

    def get_absolute_url(self):
        return reverse('owner-info', args=[str(self.owner)])


class Port(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    end = models.ForeignKey('End', db_column='end', max_length=30)  # Field name made lowercase.
    port = models.DecimalField(db_column='port', max_digits=4, decimal_places=0)  # Field name made lowercase.
    label = models.CharField(db_column='label', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='remark', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'port'
        unique_together = (('end', 'card', 'port'),)

    def __unicode__(self):
        return u'%s %s %s' % (self.end, self.port, self.label)


class RoutingCable(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    cable = models.ForeignKey('Cable', db_column='cable')  # Field name made lowercase.
    core = models.IntegerField(db_column='core')  # Field name made lowercase.
    circuit = models.ForeignKey('Circuit', db_column='circuit', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='remark', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'routing_cable'
        unique_together = (('cable', 'core'),)

    def __unicode__(self):
        return u'%s %s' % (self.cable, self.circuit)


class Termination(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    cable = models.ForeignKey('Cable', db_column='cable')  # Field name made lowercase.
    fromcore = models.IntegerField(db_column='fromcore')  # Field name made lowercase.
    is_end_a = models.DecimalField(db_column='is_end_a', max_digits=1, decimal_places=0)  # Field name made lowercase.
    is_draft = models.DecimalField(db_column='is_draft', max_digits=1, decimal_places=0)  # Field name made lowercase.
    end = models.ForeignKey('End', db_column='end', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'termination'
        unique_together = (('cable', 'isend_a', 'fromcore', 'isdraft'),)

    def __unicode__(self):
        return u'%s %s' % (self.cable, self.fromcore)
