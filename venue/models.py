from django.db import models

from mainapp import models as md
import uuid

# Create your models here.

class Venue(models.Model):

    class Meta:
        db_table = 'Venue'

    VenueID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    Owner = models.ForeignKey(md.Users, on_delete=models.SET_NULL, related_name='venue_owner',null=True)
    Name = models.CharField(max_length=100,unique=True)
    Address = models.TextField()
    City = models.ForeignKey(md.City, on_delete=models.SET_NULL,null=True)
    Latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    Longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.EmailField()
    Description = models.TextField(blank=True)
    OpeningTime = models.TimeField(null=True)
    ClosingTime = models.TimeField(null=True)
    IsActive = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name + self.Owner.FirstName

class Court(models.Model):

    class Meta:
        db_table = 'Court'

    SURFACE_TYPES = (
        ('artificial_grass', 'Artificial Grass'),
        ('concrete', 'Concrete'),
        ('wood', 'Wood'),
    )

    CourtID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, related_name='venue',null=True)
    Name = models.CharField(max_length=50)
    Description = models.TextField(blank=True)
    SportCategory = models.ForeignKey(md.SportCategory,on_delete=models.SET_NULL, null=True)
    SurfaceType = models.CharField(max_length=20, choices=SURFACE_TYPES)
    Capacity = models.PositiveIntegerField()
    HourlyRate = models.DecimalField(max_digits=8, decimal_places=2)
    IsActive = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name + self.SportCategory.SportCategory
    

class CourtImages(models.Model):

    class Meta:
        db_table = "CourtImages"  

    ImageID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    Court = models.ForeignKey(Court, on_delete=models.SET_NULL, related_name='courts_images',null=True)
    Image = models.ImageField(upload_to='court_images/', null=True, blank=True) 
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

class VenueImages(models.Model):

    class Meta:
        db_table = "VenueImages"  

    ImageID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    Venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, related_name='venue_images',null=True)
    Image = models.ImageField(upload_to='venue_images/', null=True, blank=True)  
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

class Availability(models.Model):

    class Meta:
        db_table = "Availability" 
        verbose_name_plural = "Availabilities"
        unique_together = ('Court', 'Date', 'StartTime', 'EndTime')

    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    Court = models.ForeignKey(Court, on_delete=models.SET_NULL, related_name='availabilities',null=True)
    Date = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    IsActive = models.BooleanField(default=True)
    SpecialRate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    
    
class Booking(models.Model):

    class Meta:
        db_table = "Booking" 

    BookingID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    User = models.ForeignKey(md.Users, on_delete=models.SET_NULL, related_name='bookings',null=True)
    Availability = models.ForeignKey(Availability, on_delete=models.SET_NULL, null=True)
    Status = models.ForeignKey(md.Status, on_delete=models.SET_NULL, null=True)
    PaymentMethod = models.ForeignKey(md.PaymentType, on_delete=models.SET_NULL, null=True)
    TotalPrice = models.DecimalField(max_digits=8, decimal_places=2)
    Notes = models.TextField(blank=True) 
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

class PaymentTransaction(models.Model):

    class Meta:
        db_table = "PaymentTransaction" 

    PaymentTransactionID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    Booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, related_name='transactions',null=True)
    TransactionID = models.CharField(max_length=100,unique=True)
    Amount = models.DecimalField(max_digits=8, decimal_places=2)
    PaymentStatus = models.ForeignKey(md.Status, on_delete=models.SET_NULL, null=True)
    PaymentMethod = models.ForeignKey(md.PaymentType, on_delete=models.SET_NULL, null=True)
    RawResponse = models.JSONField(null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

class VenueApplication(models.Model):

    class Meta:
        db_table = 'VenueApplication'

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Under Review' ,'Under Review'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Applicant = models.ForeignKey(md.Users, on_delete=models.SET_NULL ,related_name='venue_applications',null=True)
    VenueName = models.CharField(max_length=100)
    Address = models.TextField()
    City = models.ForeignKey(md.City, on_delete=models.SET_NULL, null=True)
    PhoneNumber = models.CharField(max_length=15)
    Email = models.EmailField()
    PanNumber = models.CharField(max_length=50)
    Status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    AdminRemark = models.TextField(blank=True, null=True)
    IsActive = models.BooleanField(default=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

class VenueApplicationDocument(models.Model):
    class Meta:
        db_table = 'VenueApplicationDocument'

    DOCUMENT_TYPE_CHOICES = (
        ('PAN Card', 'PAN Card'),
        ('Government Approval', 'Government Approval'),
        ('Business License', 'Business License'),
        ('Other', 'Other'),
    )    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Application = models.ForeignKey(VenueApplication, on_delete=models.SET_NULL, related_name='documents',null=True)
    DocumentType = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    DocumentFile = models.FileField(upload_to='venue_documents/')
    UploadedAt = models.DateTimeField(auto_now_add=True)

class OnlinePaymentKhaltiSecretKey(models.Model):

    class Meta:
        db_table = 'OnlinePaymentKhaltiSecretKey'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    Venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, related_name='khalti_keys',null=True)
    SecretKey = models.CharField(max_length=250) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


    
