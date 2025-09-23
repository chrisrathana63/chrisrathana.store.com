package com.chrisrathana.app;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;

import java.io.InputStream;
import java.nio.charset.StandardCharsets;

public class MainActivity extends AppCompatActivity {
    private WebView webView;
    private Button btnAbout, btnContact, btnConfig;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webView = findViewById(R.id.webview);
        btnAbout = findViewById(R.id.btnAbout);
        btnContact = findViewById(R.id.btnContact);
        btnConfig = findViewById(R.id.btnConfig);

        // Setup WebView
        webView.setWebViewClient(new WebViewClient());
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);

        // Load default page
        webView.loadUrl("file:///android_asset/about.html");

        btnAbout.setOnClickListener(v -> webView.loadUrl("file:///android_asset/about.html"));
        btnContact.setOnClickListener(v -> webView.loadUrl("file:///android_asset/contact.html"));
        btnAbout.setOnClickListener(v -> webView.loadUrl("file:///android_asset/review.html"));
        btnContact.setOnClickListener(v -> webView.loadUrl("file:///android_asset/product.html"));
        btnAbout.setOnClickListener(v -> webView.loadUrl("file:///android_asset/shop.html"));
        btnContact.setOnClickListener(v -> webView.loadUrl("file:///android_asset/Lonin.html"));
        btnContact.setOnClickListener(v -> webView.loadUrl("file:///android_asset/send.html"));
        btnConfig.setOnClickListener(v -> {
            String json = loadConfigFromAssets();
            // Display JSON nicely in a simple HTML wrapper
            String html = "<html><body><pre>" + escapeHtml(json) + "</pre></body></html>";
            webView.loadDataWithBaseURL(null, html, "text/html", "utf-8", null);
        });
    }

    private String loadConfigFromAssets() {
        try {
            InputStream is = getAssets().open("config.json");
            int size = is.available();
            byte[] buffer = new byte[size];
            is.read(buffer);
            is.close();
            return new String(buffer, StandardCharsets.UTF_8);
        } catch (Exception e) {
            return "{ \"error\": \"" + e.getMessage() + "\" }";
        }
    }

    private String escapeHtml(String s) {
        return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
    }
}
