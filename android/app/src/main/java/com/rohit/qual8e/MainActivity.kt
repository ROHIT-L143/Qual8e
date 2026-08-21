package com.rohit.qual8e

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.rohit.qual8e.ui.theme.Qual8eTheme

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            Qual8eTheme {
                Qual8eHomeScreen()
            }
        }
    }
}

@Composable
fun Qual8eHomeScreen() {

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {

        Text(
            text = "Qual8e",
            style = MaterialTheme.typography.headlineLarge
        )

        Spacer(modifier = Modifier.height(12.dp))

        Text(
            text = "Fast • Private • Direct",
            style = MaterialTheme.typography.bodyLarge
        )

        Spacer(modifier = Modifier.height(40.dp))

        Button(
            onClick = {
                // QR scanner will be added later
            }
        ) {
            Text("Scan QR")
        }

        Spacer(modifier = Modifier.height(16.dp))

        Button(
            onClick = {
                // File picker will be added later
            }
        ) {
            Text("Send Files")
        }

        Spacer(modifier = Modifier.height(16.dp))

        Button(
            onClick = {
                // Receive mode will be added later
            }
        ) {
            Text("Receive Files")
        }
    }
}