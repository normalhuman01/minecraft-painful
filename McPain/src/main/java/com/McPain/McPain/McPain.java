package com.McPain.McPain;
import net.minecraft.client.entity.player.*;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import net.minecraftforge.event.entity.living.LivingHurtEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.common.MinecraftForge;


import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

@Mod("mcpain")
public class McPain{

    public McPain() {
        MinecraftForge.EVENT_BUS.register(new LifeHandler());

    }

    @Mod.EventBusSubscriber
    public class LifeHandler {
        
    @SubscribeEvent
    public void checkHealth(LivingHurtEvent event){
        if (event.getEntityLiving() instanceof PlayerEntity || event.getEntityLiving() instanceof ClientPlayerEntity){
            System.out.println("AA");
            CloseableHttpClient httpClient = HttpClients.createDefault();
            try {
                HttpGet request = new HttpGet("http://127.0.0.1:5000/");
        
                System.out.println("bb");
                CloseableHttpResponse response = httpClient.execute(request);
                System.out.println(response);
            }
            catch (Exception e){
                e.printStackTrace();
            }
        }
    }

    @SubscribeEvent
    public void CheckDeath(LivingDeathEvent e){
        if (e.getEntityLiving() instanceof PlayerEntity || e.getEntityLiving() instanceof ClientPlayerEntity){
            System.out.println("AA");
            CloseableHttpClient httpClient = HttpClients.createDefault();
            try {
                HttpGet request = new HttpGet("http://127.0.0.1:5000/death");
        
                System.out.println("bb");
                CloseableHttpResponse response = httpClient.execute(request);
                System.out.println(response);
            }
            catch (Exception e){
                e.printStackTrace();
            }
        }
    }
}
}
