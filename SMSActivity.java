//"Copyright Notice and Disclaimer. 
//© NORHEASTERN UNIVERSITY 2023 SW-24013 used with permission. All rights reserved."

package de.rctrust.sms_ts;

import android.Manifest;
import android.app.Activity;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.pm.PackageManager;
import android.icu.text.SimpleDateFormat;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.os.SystemClock;
import android.telephony.CellInfo;
import android.telephony.CellInfoCdma;
import android.telephony.CellInfoGsm;
import android.telephony.CellInfoLte;
import android.telephony.CellInfoWcdma;
import android.telephony.CellSignalStrength;
import android.telephony.CellSignalStrengthCdma;
import android.telephony.CellSignalStrengthGsm;
import android.telephony.CellSignalStrengthLte;
import android.telephony.CellSignalStrengthWcdma;
import android.telephony.SmsManager;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Date;
import java.util.List;

public class SMSActivity extends AppCompatActivity {

    EditText mobile_number, text_message;
    Button send_sms, write_results;
    SmsManager sms;
    TelephonyManager manager;
    CellSignalStrength cellStrength;
    OutputStreamWriter outputStreamWriter;
    File file;

    // Make sure to:
    // (1) Define the SMS type 0.
    // (2) Perform checks to ensure that the phone state, SIM and network connection are correct.
    // (3) Create BroadcastReceivers for SENT_ACTION and DELIVERED_ACTION along with PendingIntents. 
    // (4) Collect timestamps at each stage to perform calculations later.
    // (5) Store the data in a temporary file for later processing.
}